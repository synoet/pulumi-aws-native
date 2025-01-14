// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Pipes.Outputs
{

    [OutputType]
    public sealed class PipeSourceParameters
    {
        public readonly Outputs.PipeSourceActiveMqBrokerParameters? ActiveMqBrokerParameters;
        public readonly Outputs.PipeSourceDynamoDbStreamParameters? DynamoDbStreamParameters;
        public readonly Outputs.PipeFilterCriteria? FilterCriteria;
        public readonly Outputs.PipeSourceKinesisStreamParameters? KinesisStreamParameters;
        public readonly Outputs.PipeSourceManagedStreamingKafkaParameters? ManagedStreamingKafkaParameters;
        public readonly Outputs.PipeSourceRabbitMqBrokerParameters? RabbitMqBrokerParameters;
        public readonly Outputs.PipeSourceSelfManagedKafkaParameters? SelfManagedKafkaParameters;
        public readonly Outputs.PipeSourceSqsQueueParameters? SqsQueueParameters;

        [OutputConstructor]
        private PipeSourceParameters(
            Outputs.PipeSourceActiveMqBrokerParameters? activeMqBrokerParameters,

            Outputs.PipeSourceDynamoDbStreamParameters? dynamoDbStreamParameters,

            Outputs.PipeFilterCriteria? filterCriteria,

            Outputs.PipeSourceKinesisStreamParameters? kinesisStreamParameters,

            Outputs.PipeSourceManagedStreamingKafkaParameters? managedStreamingKafkaParameters,

            Outputs.PipeSourceRabbitMqBrokerParameters? rabbitMqBrokerParameters,

            Outputs.PipeSourceSelfManagedKafkaParameters? selfManagedKafkaParameters,

            Outputs.PipeSourceSqsQueueParameters? sqsQueueParameters)
        {
            ActiveMqBrokerParameters = activeMqBrokerParameters;
            DynamoDbStreamParameters = dynamoDbStreamParameters;
            FilterCriteria = filterCriteria;
            KinesisStreamParameters = kinesisStreamParameters;
            ManagedStreamingKafkaParameters = managedStreamingKafkaParameters;
            RabbitMqBrokerParameters = rabbitMqBrokerParameters;
            SelfManagedKafkaParameters = selfManagedKafkaParameters;
            SqsQueueParameters = sqsQueueParameters;
        }
    }
}
