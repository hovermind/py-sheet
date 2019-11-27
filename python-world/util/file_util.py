# -*- coding:utf-8 -*-
"""\
File utility module.
"""
from typing import List, Tuple, Union
from pathlib import Path
import shutil
from util import log_util

CONSOLE_LOGGER = log_util.get_console_logger(__name__)


def log_error_console(exception: OSError):
    """\
    Logs error messages to console.

    Args:
        exception (OSError): exception object
    """
    CONSOLE_LOGGER.error("Error: %(filename)s - %(strerror)s",
                         {
                             "filename": exception.filename,
                             "strerror": exception.strerror
                         })
    # ---
    # END: log_error_console


def dir_exists(dir_path: Path) -> bool:
    """
    Checks if directory exists for given uri.

    Args:
        dir_path (Path): directory path uri

    Returns:
        bool - True if exists, False otherwise
    """
    return dir_path.exists() and dir_path.is_dir()
    # ---
    # END: dir_exists


def resolve_dir(file_uri: str) -> Path:
    """\
    Resolves directory for given file path.

    Args:
        file_uri (str): file path with extension

    Returns :
        str: directory uri that contains the given file.
    """
    return Path(file_uri).resolve().parent
    # ---
    # END: resolve_dir


def create_dirs(dir_paths: List[Path]):
    """\
    Creates directories for given directory name lists.

    Args:
        dir_paths (List[Path]) : directory name list
    """
    if len(dir_paths) > 0:
        try:
            for dir_uri in dir_paths:
                dir_uri.mkdir(parents=True, exist_ok=True)
        except OSError as ex:
            log_error_console(exception=ex)
    # ---
    # END: create_dirs


def file_exists(file_uri: str):
    """\
    Checks if a file exists or not.

    Args:
        file_uri (str): file path with extension.
    """
    path: Path = Path(file_uri)
    return path.exists() and path.is_file()
    # ---
    # END: file_exists


def copy_files(file_tuple_list: List[Tuple[str, str]]):
    """\
    Iterates over given tuple list and copies files from target to destination.

    Args:
        file_tuple_list (List[(str, str)]): list of (target, destination) Tuple.
    """
    if len(file_tuple_list) > 0:
        try:
            for file_tuple in file_tuple_list:
                (src, destination) = file_tuple
                destination_path = Path(destination)
                destination_path.symlink_to(src)
        except OSError as ex:
            log_error_console(exception=ex)
    # ---
    # END: copy_files


def remove_files(dir_path: Path, file_extension: str):
    """\
    Removes all files of given type (i.e. xxx.fastq) from the specified folder.

    Args:
        dir_path (Path): directory uri
        file_extension (str): type of files to remove (i.e. 'xxx.txt')
    """
    file_paths: List[Path] = list(dir_path.glob(f"*.{file_extension}"))

    for target_file in file_paths:
        try:
            target_file.unlink()  # removes a file or symbolic link
        except OSError as ex:
            log_error_console(exception=ex)
    # ---
    # END: remove_files


def delete_dir(dir_path: Union[str, Path]):
    """\
    Deletes all file in a directory and directory itself.

    Args:
        dir_path (Union[str, Path]) : directory to delete
    """
    try:
        # normalise
        if isinstance(dir_path, str):
            dir_path = Path(dir_path)
        if dir_path.exists():
            # https://code-examples.net/en/q/b28941
            if dir_path.is_symlink():
                dir_path.unlink()
            else:
                shutil.rmtree(dir_path)
    except OSError as ex:
        log_error_console(exception=ex)
    # ---
    # END: delete_dir


def fetch_file_list(dir_path: Path, pattern: str) -> List[Path]:
    """\
    Fetches file list for specified directory.

    Args:
        dir_path (Path) : target directory
        pattern (str) : pattern to match
    """
    file_list: List[Path] = []

    if dir_exists(dir_path):
        file_list = list(dir_path.glob(pattern))

    return file_list
    # ---
    # END: fetch_file_list


def not_empty_dir(dir_path: Path, file_extension: str = "*") -> bool:
    """\
    Checks if the given directory is empty or not.

    Args:
        dir_path (str) : name of the directory
        file_extension (str) : file type

    Returns:
        bool - True is directory is empty, False otherwise
    """
    files_in_dir = fetch_file_list(dir_path, pattern=f"*.{file_extension}")

    return len(files_in_dir) > 0
    # ---
    # END: not_empty_dir


def create_files(dir_path: Path, files: List[str]):
    """\
    Creates files in the given directory.

    Args:
        dir_path (Path) : target directory
        files (List[str]) : list of file names
    """
    # create dir if not exists
    try:
        if not dir_exists(dir_path):
            create_dirs([dir_path])

        for file_uri in files:
            dir_path.joinpath(file_uri).touch()

    except OSError as ex:
        log_error_console(exception=ex)
    # ---
    # END: create_files


def create_files_ext(dir_path: Path, files: List[str], extension: str = None):
    """\
    Creates files with specified extension in the given directory.

    Args:
        dir_path (str) : target directory
        files (List[str]) : list of file names with
        extension (str): file extension
    """
    if extension:
        # add extension
        files_with_ext: List[str] = []
        for file in files:
            files_with_ext.append(f"{file}.{extension}")

        create_files(dir_path, files_with_ext)
    else:
        create_files(dir_path, files)


def append_to_file(file_uri: Union[Path, str], data: object):
    """\
    Appends data to the given file.

    Args:
        file_uri (str) : file (with extension) to append data
        data (object) : data as string with words separated by tabs
    """
    if not file_exists(file_uri):
        return  # early exit

    # append data to file
    with open(file_uri, mode='a') as append_file:
        append_file.write(f"\n{str(data)}")
    # ---
    # END: append_to_file


def delete_files(file_uri_list: List[Path]):
    """\
    Deletes files in given (or current) directory.

    Args:
        file_uri_list (List[Path]): file (with extension) list
    """
    # perform delete operation
    for file_uri in file_uri_list:
        file_uri.unlink()
    # ---
    # END: delete_files


def delete_files_in_dir(dir_path: Path, file_pattern: str = "*.*"):
    """\
    Deletes files in the given directory.

    Args:
        dir_path (Path): directory uri
        file_pattern (str): All matching file patterns
    """
    # perform delete operation
    if dir_exists(dir_path):
        try:
            file_list = fetch_file_list(dir_path, file_pattern)
            delete_files(file_list)
        except OSError as ex:
            log_error_console(exception=ex)
    # ---
    # END: delete_files_in_dir
