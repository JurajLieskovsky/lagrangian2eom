from sympy import diff, hessian


def massMatrix(T, q, t):
    """
    Derives the mass matrix of the system

    Parameters
    ----------
    T: sympy function
        kinetic energy of the system
    q: sympy column vector
        vector of generalized coordinates
    t: sympy symbol
        time symbol
    Returns
    -------
    M: sympy matrix
        mass matrix
    """
    return hessian(T, diff(q, t))


def velocityTerms(T, q, t):
    """
    Derives torques tied to the kinetic energy of the system

    Parameters
    ----------
    T: sympy function
        kinetic energy of the system
    q: sympy column vector
        vector of generalized coordinates
    t: sympy symbol
        time symbol
    Returns
    -------
    c: sympy column vector
        vector of corriolis and centrifugal torques
    """
    return diff(T, diff(q, t).T).jacobian(q) * diff(q, t) - diff(T, q)


def potentialTerms(V, q):
    """
    Derives torques tied to the potential energy of the system

    Parameters
    ----------
    V: sympy function
        potential energy of the system
    q: sympy column vector
        vector of generalized coordinates
    Returns
    -------
    tau_p: sympy column vector
        vector of potential fields' torques
    """
    return -diff(V, q)


def wrenchMatrix(r, q):
    """
    Derives the wrench matrix for a moment arm of an external force acting on the system

    Parameters
    ----------
    r: sympy column vector
        moment arm
    q: sympy column vector
        generalized coordinates

    Returns
    -------
    W: sympy matrix
        wrench matrix
    """
    return r.jacobian(q)
