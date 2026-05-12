"""Job agendado para reengajamento de usuários inativos via Telegram."""

from apscheduler.schedulers.background import BackgroundScheduler

from agente_telegram.bot import bot_telegram
from agente_telegram.service.users_history import UserHistoryService


scheduler = BackgroundScheduler()


def job():
    """Busca usuários inativos há mais de 2 dias e envia mensagem de reengajamento.

    Processa em lotes de 20 usuários, marcando cada um como notificado
    para evitar envios duplicados. Execução agendada diariamente às 8h.
    """
    user_history = UserHistoryService()

    for users in user_history.yield_inactive_users_for_processing():

        for user in users:

            print(user.id_user)

            bot_telegram.send_mensage(
                user.id_user,
                "Olá, não nos falamos a muito tempo, vamos conversar?"
            )

            user.notification_inactivity = True

scheduler.add_job(
    job,
    'cron',
    hour=8)


if __name__ == '__main__':
    job()



