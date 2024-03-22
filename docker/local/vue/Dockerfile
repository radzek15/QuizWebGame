ARG IMAGE=node:bookworm-slim

FROM ${IMAGE} as client-build

ARG APP_HOME=/app

WORKDIR ${APP_HOME}

COPY ./client/package.json ./client/yarn.lock ./

RUN yarn install

COPY ./client/ ./

CMD ["yarn","serve"]
