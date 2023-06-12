primeira = float(input('Digite sua primeira nota: '))
segunda = float(input('Digite sua segunda nota: '))
media = (primeira + segunda) / 2

if media <= 5:
    print('\033[1;31mInfelizmente, sua média foi {:.1f} e você está reprovado!'.format(media))
elif media >= 5 and media < 6.9:
    print('\033[1;33mSua média foi {:.1f} e você está de recuperação'.format(media))
else:
    print('\033[1;32mParabéns! Sua média foi {:.1f} e você foi aprovado'.format(media))
