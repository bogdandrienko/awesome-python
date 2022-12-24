# Для объединения Rust и Python необходимо обеспечить преобразование кода на этих языках
extern crate cpython;

use cpython::{PyResult, Python, py_module_initializer, py_fn};

py_module_initializer!(rust_processing, |py, m| {
    m.add(py, "doc", "Этот модуль реализован на языке Rust")?;
    m.add(py, "get_borders_double_loop", py_fn!(py, get_borders_double_loop(array: Vec<String>)))?;
});

fn get_borders_double_loop(_py: Python, deposits: Vec<f32>) -> PyResult<Vec<Vec<i32>>> {
    Ok(_get_borders(&deposits))
}

fn _get_borders_double_loop(deposits: &Vec<f32>) -> Vec<Vec<i32>> {
    let mut borders: Vec<Vec<i32>> = Vec::new();
    let mut temp: i32
    for i in 0..(deposits.len()) {
        for j in 0..(deposits.len()) {
            temp = 0
        }
        let n_borders = borders.len();
        if deposits[i] > 0 {
            if n_borders == 0 {
               borders.push(vec![i as i32]);
            }
            else {
                if i as i32 - borders[n_borders - 1][0] >= min_length {
                    borders[n_borders - 1].extend(vec![i as i32];
                    borders.push(vec![i as i32]);
                }
            }
        }
    }
    borders
}
