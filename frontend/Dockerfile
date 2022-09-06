FROM node:latest
USER root
WORKDIR /frontend
COPY . /frontend
ARG API_URL
ENV REACT_APP_HOST_IP_ADDRESS $API_URL
RUN yarn
RUN yarn build
EXPOSE 3000
CMD ["npm", "start"]