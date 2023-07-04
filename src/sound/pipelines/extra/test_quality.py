import pandas as pd
import pytest

# Récupération des données du fichier csv
df = pd.read_csv('data/01_raw/examens_tonaux.csv')

def test_dataframe_columns():
    # Vérifiez les colonnes existantes
    expected_columns = ['before_exam_125_Hz', 'before_exam_250_Hz', 'before_exam_500_Hz', 'before_exam_1000_Hz','before_exam_2000_Hz', 'before_exam_4000_Hz', 'before_exam_8000_Hz',
                        'after_exam_125_Hz', 'after_exam_250_Hz', 'after_exam_500_Hz', 'after_exam_1000_Hz', 'after_exam_2000_Hz', 'after_exam_4000_Hz',
                        ]
    assert df.columns.tolist() == expected_columns

    # Vérifiez l'absence de colonnes en trop
    assert len(df.columns) == len(expected_columns)
    
pytest.main()