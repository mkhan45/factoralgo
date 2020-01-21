use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

#[pyfunction]
// trial and error because euler's is too big brain
fn gcd(mut a: u128, mut b: u128) -> u128 {
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
// test i and i + 2 for all the numbers from 5..11..17 etc. to sqrt(n)
// i.e. 5..7..11..13..17..19..23..25 etc.
fn isprime(n: u128) -> bool {
    n == 2 || n == 3 || (n % 2 != 0 && n % 3 != 0 && n % 5 != 0 && (5..(n as f32).sqrt() as u128).step_by(6).all(|i|{
        n % i != 0 && n % (i + 2) != 0
    }))
}

#[pymodule]
fn factoralgo(py: Python, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(gcd))?;
    m.add_wrapped(wrap_pyfunction!(isprime))?;
    Ok(())
}
