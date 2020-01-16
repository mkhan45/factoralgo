use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

#[pyfunction]
fn gcd(mut a: usize, mut b: usize) -> usize {
    if a == 0 || b == 0 {
        return 0
    }
    if a > b {
        let c = a;
        a = b;
        b = c;
    }

    let remainder = b % a;

    if remainder != 0 {
        gcd(a, remainder)
    } else {
        a
    }
}

#[pyfunction]
fn isprime(n: usize) -> bool {
    n == 2 || (n % 2 != 0 && (3..(1 + (n as f32).sqrt().round() as usize)).step_by(2).all(|i|{
        n % i != 0
    }))
}

#[pymodule]
fn factoralgo(py: Python, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(gcd))?;
    m.add_wrapped(wrap_pyfunction!(isprime))?;
    Ok(())
}
