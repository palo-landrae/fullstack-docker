# Stage 1: Compile and Build angular codebase

# Use latest node image as the base image
FROM node:16-alpine as builder

# Set the working directory
WORKDIR '/app' 

# Install all the dependencies 
COPY ./package.json ./   
RUN npm install
RUN npm i -g @angular/cli

# Add the source code to app
COPY . .

# Generate the build of the application
RUN npm run build

# Stage 2: Serve app with nginx server

# Use official nginx image as the base image
FROM nginx:alpine

# Copy the build output to replace the default nginx contents.
COPY --from=builder /app/dist/frontend /usr/share/nginx/html

# Expose port 80
EXPOSE 80