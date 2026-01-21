"""
Tests for file processing utilities
"""

import pytest
from utils.file_processor import process_uploaded_file, get_file_summary


class MockFile:
    """Mock file object for testing"""
    def __init__(self, name, content):
        self.name = name
        self.content = content
    
    def read(self):
        return self.content.encode() if isinstance(self.content, str) else self.content


def test_process_text_file():
    """Test processing of text files"""
    mock_file = MockFile("test.txt", "This is a test file")
    result = process_uploaded_file(mock_file)
    assert "This is a test file" in result


def test_process_markdown_file():
    """Test processing of markdown files"""
    mock_file = MockFile("test.md", "# Header\n\nContent")
    result = process_uploaded_file(mock_file)
    assert "# Header" in result


def test_unsupported_file_type():
    """Test handling of unsupported file types"""
    mock_file = MockFile("test.xyz", "content")
    result = process_uploaded_file(mock_file)
    assert "Unsupported file type" in result


def test_get_file_summary():
    """Test file summary generation"""
    file_data = {
        'name': 'test.txt',
        'content': 'This is test content with multiple words.\nAnd multiple lines.'
    }
    summary = get_file_summary(file_data)
    assert 'test.txt' in summary
    assert 'words' in summary


# Add more tests as needed:
# - PDF processing
# - PPTX processing
# - Excel processing
# - CSV processing
# - Error handling
