import pandas as pd
import pytest

# Récupération des données du fichier csv
data = {
    'before_exam_125_Hz': [49, 33, 82],
    'before_exam_250_Hz': [65, 57, 77],
    'before_exam_500_Hz': [102, 23, 107],
    'before_exam_1000_Hz': [54, 44, 81],
    'before_exam_2000_Hz': [92, 31, 26],
    'before_exam_4000_Hz': [97, 81, 60],
    'before_exam_8000_Hz': [100, 81, 90],
    'after_exam_125_Hz': [48, 18, 40],
    'after_exam_250_Hz': [59, 54, 28],
    'after_exam_500_Hz': [52, 19, 82],
    'after_exam_1000_Hz': [29, 36, 73],
    'after_exam_2000_Hz': [88, 20, 20],
    'after_exam_4000_Hz': [75, 60, 29],
    'after_exam_8000_Hz': [75, 58, 67]
}

df = pd.DataFrame(data)


def test_dataframe_columns():
    # Vérifiez les colonnes existantes
    expected_columns = ['before_exam_125_Hz', 'before_exam_250_Hz', 'before_exam_500_Hz', 'before_exam_1000_Hz','before_exam_2000_Hz', 'before_exam_4000_Hz', 'before_exam_8000_Hz',
                        'after_exam_125_Hz', 'after_exam_250_Hz', 'after_exam_500_Hz', 'after_exam_1000_Hz', 'after_exam_2000_Hz', 'after_exam_4000_Hz', 'after_exam_8000_Hz'
                        ]
    assert df.columns.tolist() == expected_columns

    # Vérifiez l'absence de colonnes en trop
    assert len(df.columns) == len(expected_columns)
    
pytest.main()