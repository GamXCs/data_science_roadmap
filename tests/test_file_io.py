from src.week1.file_io import read_lines


# ----------- read_lines --------------
def test_base_case_readfile(tmp_path):
    f = tmp_path / "test.txt"
    f.write_text("hello\nworld\n")
    assert read_lines(str(f)) == ["hello", "world"]


def test_base_no_readfile(tmp_path):
    assert read_lines(str(tmp_path / "ghost.txt")) == []
