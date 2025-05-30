import pytest

# develop your test cases here

@pytest.mark.unit
def test_detect_duplicates():
    assert True

@pytest.mark.unit
def test_detect_duplicates_empty():
    with pytest.raises(ValueError):
        from src.util.detector import detect_duplicates
        detect_duplicates("")

@pytest.mark.unit
def test_detect_duplicates_single_article():
    with pytest.raises(ValueError):
        from src.util.detector import detect_duplicates
        data = """
            @article{key1,
                title={Article 1},
                author={Author A},
                year={2020}
            }
        """
        detect_duplicates(data)

@pytest.mark.unit
def test_detect_duplicates_missing_doi_same_key():
    from src.util.detector import detect_duplicates
    data = """
    @article{key1,
        title={Article 1},
        author={Author A},
        year={2020}
    }
    @article{key2,
        title={Article 2},
        author={Author B},
        year={2021}
    }
    @article{key1,
        title={Article 2},
        author={Author B},
        year={2021}
    }
    """
    duplicates = detect_duplicates(data)
    assert len(duplicates) == 2

@pytest.mark.unit
def test_detect_duplicates_same_key_one_missing_doi():
    from src.util.detector import detect_duplicates
    data = """
    @article{key1,
        title={Article 1},
        author={Author A},
        year={2020}
    }
    @article{key1,
        title={Article 2},
        author={Author B},
        year={2021}
    }
    @article{key2,
        title={Article 3},
        author={Author C},
        year={2022},
        doi={10.1000/xyz789}
    }
    """
    duplicates = detect_duplicates(data)
    assert len(duplicates) == 2

@pytest.mark.unit
def test_detect_no_duplicates_missing_doi():
    from src.util.detector import detect_duplicates
    data = """
    @article{key1,
        title={Article 1},
        author={Author A},
        year={2020},
    }
    @article{key2,
        title={Article 2},
        author={Author B},
        year={2021},
    }
    """
    duplicates = detect_duplicates(data)
    assert len(duplicates) == 0

@pytest.mark.unit
def test_detect_duplicates_same_doi():
    from src.util.detector import detect_duplicates
    data = """
    @article{key1,
        title={Article 1},
        author={Author A},
        year={2020},
        doi={10.1000/xyz123}
    }
    @article{key2,
        title={Article 2},
        author={Author B},
        year={2021},
        doi={10.1000/xyz123}
    }
    """
    duplicates = detect_duplicates(data)
    assert len(duplicates) == 2