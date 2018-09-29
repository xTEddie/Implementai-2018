FROM node:carbon

WORKDIR /app

COPY . /app

RUN yarn install

RUN yarn build

EXPOSE 3000

CMD ["node", "app.js"]
