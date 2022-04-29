# goddady

EMR Instance Management

## Scheme
### Models
#### 1. TaskQueue
#### 2. Team
#### 3. Environment
#### 4. EnvironmentInstance
#### 5. EMR

### Serializers
#### 1. TeamSerializer
#### 2. EnvironmentSerializer
#### 3. EnvironmentInstanceSerializer
#### 4. EMRSerializer

### CommandManagement
```
Define Commands for running Tasks in TaskQueues to create, update, or delete EMR instance.
We will have TaskRunnser using Bot3 so that we will run task directly.
Every 5 mins, we will check TaskQueues by using Cron.
```

## TODO
1. Define TaskRunner
2. Command Management
3. Specify Serializer
4. Specify APIViewSets
5. Enhance Security

