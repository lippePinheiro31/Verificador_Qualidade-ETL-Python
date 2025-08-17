regras = {
    "cpf": {"tipo": "string", "tamanho": 11, "obrigatorio": True},
    "email": {"tipo": "string", "obrigatorio": True, "regex": r".+@.+"},
    "idade": {"tipo": "int", "min": 0, "max": 120},
    "nome": {"tipo": "string", "obrigatorio": True}
}