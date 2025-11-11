CREATE OR REPLACE MODEL `Modelo_costas.modelo_costas_lr`
OPTIONS (
  model_type = 'linear_reg',
  input_label_cols = ['COSTAS'],
  data_split_method = 'RANDOM',
  data_split_eval_fraction = 0.20,
  category_encoding_method = 'DUMMY_ENCODING',  
  calculate_p_values = TRUE
) AS
SELECT
  CUANTIA,
  COSTAS
FROM `Modelo_costas.datos`;
