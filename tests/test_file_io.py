from src.week1.file_io import (
    append_line,
    read_lines,
    read_nonempty,
    word_count,
    write_lines,
)


# ----------- read_lines --------------
def test_base_case_readfile(tmp_path):
    f = tmp_path / "test.txt"
    f.write_text("hello\nworld\n")
    assert read_lines(str(f)) == ["hello", "world"]


def test_base_no_readfile(tmp_path):
    assert read_lines(str(tmp_path / "ghost.txt")) == []


# --------- write_lines ---------------
# to check if this function works, write to the file & read it back
# tmp_path gives read_text() to be able to read the file
def test_write_lines(tmp_path):
    f = tmp_path / "test.txt"
    words = ["this", "is", "a", "test"]
    write_lines(str(f), words)
    assert f.read_text() == "this\nis\na\ntest\n"


# empty list returns an empty string
def test_write_lines_empty_list(tmp_path):
    f = tmp_path / "test.txt"
    word_list = []
    write_lines(str(f), word_list)
    assert f.read_text() == ""


# ------------ append_line ---------------
# write to file, call append_line, check if both are present
def test_append_line_basic(tmp_path):
    f = tmp_path / "test.txt"
    word_test = ["test", "text"]
    write_lines(str(f), word_test)
    append_line(str(f), "listtest")
    assert f.read_text() == "test\ntext\nlisttest\n"


def test_append_line_twice(tmp_path):
    f = tmp_path / "test.txt"
    f.write_text("first\n")
    append_line(str(f), "second")
    append_line(str(f), "third")
    assert f.read_text() == "first\nsecond\nthird\n"


# ---------- word_count --------------
def test_word_count(tmp_path):
    f = tmp_path / "test.txt"
    f.write_text("I need I")
    assert word_count(str(f)) == {"i": 2, "need": 1}


def test_word_count_with_punctuation(tmp_path):
    f = tmp_path / "test.txt"
    f.write_text("I.- I,! hi")
    assert word_count(str(f)) == {"i": 2, "hi": 1}


# ---------- readnonempty ---------------
def test_read_nonempty():
    pass


def test_read_nonempty():
    pass
