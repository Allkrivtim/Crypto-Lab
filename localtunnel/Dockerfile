# Используем официальный Node.js образ
FROM node:18

# Устанавливаем LocalTunnel
RUN npm install -g localtunnel

# Запускаем LocalTunnel
CMD ["lt", "--port", "80", "--subdomain", "cryptolabgamebotsitetest"]