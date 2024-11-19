# Essa atividade  aborda conceitos básicos utilização Funçoes em Python,
# exemplicafica detalhadamente um codigo pequeno e bem simples para 
# entendimento de estrutura com condiçoes e funçoes, .


def loginUsuario(perfil):
  """Verifica o perfil do usuário e imprime uma mensagem de boas-vindas.

  Args:
    perfil: O perfil do usuário (admin ou outro).
  """

  perfil_minusculo = perfil.lower()
  if perfil_minusculo == "user":
    print("Bem-vindo, Administrador!")
  else:
    print("Bem-vindo, Usuário!")

# abaixo os testes Chamando a função com diferentes perfis.
loginUsuario("Admin")
#loginUsuario("admin")
#loginUsuario("User")
#loginUsuario("usuário")