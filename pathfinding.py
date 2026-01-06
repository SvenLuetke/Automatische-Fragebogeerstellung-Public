import pathlib
import os
from typing import Optional

def get_single_word_document_path(directory_path: str) -> Optional[pathlib.Path]:

    folder = pathlib.Path(directory_path)
    if not folder.is_dir():
        raise FileNotFoundError(f"The specified directory does not exist or is not a folder: {directory_path}")

    WORD_EXTENSIONS = ('.docx', '.doc')

    all_files = [p for p in folder.iterdir() if p.is_file()]
    
    if not all_files:
        raise ValueError(f"Error: The folder '{directory_path}' is empty. Cannot find any Word document.")
    
    if len(all_files) > 1:
        file_names = [f.name for f in all_files]
        raise ValueError(
            f"Error: The folder '{directory_path}' contains too many files ({len(all_files)} total files). "
            f"Please ensure it contains only a single Word document. Files found: {', '.join(file_names)}"
        )

    single_file = all_files[0]
    
    if single_file.suffix.lower() not in WORD_EXTENSIONS:
        raise ValueError(
            f"Error: The only file found, '{single_file.name}', is not a Word document. "
            f"Expected extensions: {', '.join(WORD_EXTENSIONS)}"
        )
        
    print(f"Success: Found exactly one Word document: {single_file.name}")
    return single_file


get_single_word_document_path('Input')