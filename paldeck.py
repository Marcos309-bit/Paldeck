nome =input("Digite Seu Nome:")
print(f"pawldex de {nome}")

quantidade_pawl = int(input("Quantos pawls você tem?"))
print(f"{nome} possui {quantidade_pawl} pawls")

inserir = int(input("Quantos novos voçê capturou?"))

nova_quntidade = quantidade_pawl + inserir

print(f"{nome} capturou {inserir} pawls novos e agora tem {nova_quntidade}")
