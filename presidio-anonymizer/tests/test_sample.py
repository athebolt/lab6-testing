import pytest
from presidio_anonymizer.sample import sample_run_anonymizer

def test_sample_run_anonymizer():
    result = sample_run_anonymizer("My name is Bond.", 11, 15)
    
    assert result.__getattribute__("text") == "My name is BIP."
    assert result.__getattribute__("items")[0].start == 11
    assert result.__getattribute__("items")[0].end == 14
    assert result.__getattribute__("items")[0].entity_type == 'PERSON'
    assert result.__getattribute__("items")[0].text == 'BIP'
    assert result.__getattribute__("items")[0].operator == 'replace'