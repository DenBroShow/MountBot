import bot.module as module
import random


def on_command(data, user, msg):
    msg.enable_nickname()
    if len(data['args']) < 2:
        error('используйте: Казино <ставка> ⚠')
    bet = user.input(data['args'][1])
    if bet is None:
        error('используйте: Казино <ставка> ⚠')
    user.take_money(bet)
    if random.randint(0, 100) < 50:
        msg.add_lines([
            "поздравляем, вы победили! 🤑",
            "💶 Ваша прибыль: {}$".format(module.utils.digit_number(bet))
        ])
        user.add('balance', bet * 2)
    else:
        msg.add_lines([
            "к сожалению, вы проиграли 😵",
            "➖ Ваша ставка обнуляется"
        ])


cmd = {
    'name': 'казино',
    'processing': on_command
}
