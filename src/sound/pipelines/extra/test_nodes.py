import pandas as pd
import pytest

from .nodes import normalise_data

# Récupération des données du fichier csv
data = {
    'before_exam_125_Hz': [49, 33, 82],
    'before_exam_250_Hz': [65, 57, None],
    'before_exam_500_Hz': [102, 23, 107],
    'before_exam_1000_Hz': [54, 44, 81],
    'before_exam_2000_Hz': [92, 31, 26],
    'before_exam_4000_Hz': [97, 81, 60],
    'before_exam_8000_Hz': [100, 81, 90],
    'after_exam_125_Hz': [48, 18, 40],
    'after_exam_250_Hz': [59, 61, 28],
    'after_exam_500_Hz': [52, 19, 82],
    'after_exam_1000_Hz': [29, 61, 73],
    'after_exam_2000_Hz': [88, 20, 20],
    'after_exam_4000_Hz': [75, 60, 29],
    'after_exam_8000_Hz': [75, 58, 67]
}

df = pd.DataFrame(data)

def test_clean_data():
    #Vérification des valeurs nulles -> suppresion des lignes (alerte)    
    assert len(df.dropna()) == len(df) - 1

def test_normalise_data():
    #Vérification des valeurs nulles -> suppresion des lignes (alerte)
    normalised_dataframe = normalise_data(df) 
    min_values = normalised_dataframe.min().min()
    max_values = normalised_dataframe.max().min()

    assert min_values == 0
    assert max_values == 1

#def split_data():
    #Vérification des valeurs nulles -> suppresion des lignes (alerte)    
    #assert len(df.dropna()) == len(df) - 1
    
pytest.main()