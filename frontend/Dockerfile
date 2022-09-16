FROM node:latest
USER root
WORKDIR /frontend
COPY package*.json ./
ARG API_URL
ENV REACT_APP_HOST_IP_ADDRESS $API_URL

RUN npm install
# RUN yarn
# RUN yarn build
EXPOSE 3000

