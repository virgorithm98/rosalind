import pytest
from main.ini_3 import string_slicing


def test_string_slicing():
    assert string_slicing("HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.", 22, 27, 97, 102) == "Humpty Dumpty"
    with pytest.raises(ValueError, match="First number is greater than the second number"):
        string_slicing("ADAaRHCeR3eYI0OWckZuwt86x7ARGrM8eEXSEY6gS5alJ8zCircusaRT4b7FtGPJqIFDbBON1FdXiWvG2THqJ2dV3nIjuu2sLkHy5RjiQhsansPWg4UgzOfHLyoX0Dg6fKytoLGw1DdOWu4q85ApUlT0VdoWhmUMzho8mcIEptkfuH3H8Qtm2YZYheliacaVIkdW2.", 3, 1, 57, 67)
    with pytest.raises(ValueError, match="First number is greater than the second number"):
        string_slicing("ADAaRHCeR3eYI0OWckZuwt86x7ARGrM8eEXSEY6gS5alJ8zCircusaRT4b7FtGPJqIFDbBON1FdXiWvG2THqJ2dV3nIjuu2sLkHy5RjiQhsansPWg4UgzOfHLyoX0Dg6fKytoLGw1DdOWu4q85ApUlT0VdoWhmUMzho8mcIEptkfuH3H8Qtm2YZYheliacaVIkdW2.", 1, 3, 67, 57)