FROM public.ecr.aws/lambda/python:3.8

RUN pip install awslambdaric

RUN pip install pandas xlsxwriter serverless-wsgi flask boto3

COPY . ./

CMD ["serverless_handler.handler"]