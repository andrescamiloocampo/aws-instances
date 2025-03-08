import boto3

client = boto3.client(
        's3',
        region_name='us-east-1',    
)

ec2_client = boto3.client(
        'ec2',
        region_name='us-east-1'
)

bucket = 'andres-ocampo-bucket'

def upload_object():    
    try:
        response = client.upload_file(
            './hola_mundo.txt',         
            'andres-ocampo-bucket',     
            'hola_mundo'                
        )
        print("Archivo subido exitosamente!")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def validate_object(name):
    try:
        response = client.head_object(Bucket = bucket,Key = name)
        print(f"El objeto '{name}' existe en el bucket '{bucket}'.")
    except Exception as e:        
        print(f"No se pudo encontrar el objeto en el bucket")

def create_bucket(name):
    try:        
        response = client.create_bucket(
            Bucket=name
        )
        print(f"Bucket creado exitosamente")
        print(response)
    except Exception as e:
        print("Error al crear el bucket",e)

def create_machine():
    try:
        response = ec2_client.run_instances(
            ImageId='ami-08b5b3a93ed654d19',
            InstanceType='t2.micro',
            MinCount=1,
            MaxCount=1,
            KeyName='andres-access',
            SecurityGroupIds=['sg-0e3953b123bceb276'],  
            SubnetId='subnet-0b52b1b8bbad243b8',       
            TagSpecifications=[            
                {
                    'ResourceType': 'instance',
                    'Tags': [
                        {
                            'Key': 'Name',
                            'Value': 'andres-ocampo-instance'
                        },
                    ]
                },
            ]
        )
        instance_id = response['Instances'][0]['InstanceId']
        print(f"Instancia EC2 creada con ID: {instance_id}")
        return instance_id
    except Exception as e:
        print(f"Error al crear la instancia EC2: {e}")
        return None

def main_loop():
    print("Ingrese 1 para crear un bucket")
    print("Ingrese 2 para crear una instancia")
    print("Ingrese 0 para no hacer nada")
    opt = int(input("Ingrese un numero:"))
    if opt == 1:
        name = input("Ingrese el nombre del bucket:")
        create_bucket(name)
    if opt == 2:
        create_machine()

main_loop()

