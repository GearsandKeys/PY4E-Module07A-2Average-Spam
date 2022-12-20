import average_spam_confidence

def test_short_mbox_output(capfd, monkeypatch):
    input = ['mbox-short.txt']
    monkeypatch.setattr('builtins.input', lambda _:input.pop())
    average_spam_confidence.print_count_of_spam_confidence()
    out, err = capfd.readouterr()
    assert "Average spam confidence: 0.7507185185185187" in out

def test_long_mbox_output(capfd, monkeypatch):
    input = ['mbox-long.txt']
    monkeypatch.setattr('builtins.input', lambda _:input.pop())
    average_spam_confidence.print_count_of_spam_confidence()
    out, err = capfd.readouterr()
    assert "Average spam confidence: 0.8941280467445736" in out
