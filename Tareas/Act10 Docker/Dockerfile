FROM node:18

WORKDIR /app

COPY package*.json ./
COPY server.js ./
COPY public/ ./public/

RUN npm install

EXPOSE 3000

CMD ["node", "server.js"]
