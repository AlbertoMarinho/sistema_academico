import re

def validar_cpf(cpf):
    """Valida um CPF (formato básico)"""
    if not cpf:
        return False
    
    # Remove caracteres não numéricos
    cpf = re.sub(r'[^0-9]', '', cpf)
    
    # Verifica se tem 11 dígitos
    if len(cpf) != 11:
        return False
    
    # Verifica se todos os dígitos são iguais
    if cpf == cpf[0] * 11:
        return False
    
    return True

def validar_email(email):
    """Valida um email"""
    if not email:
        return False
    
    # Pattern básico de email
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validar_telefone(telefone):
    """Valida um telefone (formato básico)"""
    if not telefone:
        return True  # Telefone é opcional
    
    # Remove caracteres não numéricos
    telefone = re.sub(r'[^0-9]', '', telefone)
    
    # Verifica se tem entre 10 e 11 dígitos
    return len(telefone) in [10, 11]