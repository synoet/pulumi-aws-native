// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.ElastiCache.Inputs
{

    /// <summary>
    /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-nodegroupconfiguration.html
    /// </summary>
    public sealed class ReplicationGroupNodeGroupConfigurationArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-nodegroupconfiguration.html#cfn-elasticache-replicationgroup-nodegroupconfiguration-nodegroupid
        /// </summary>
        [Input("NodeGroupId")]
        public Input<string>? NodeGroupId { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-nodegroupconfiguration.html#cfn-elasticache-replicationgroup-nodegroupconfiguration-primaryavailabilityzone
        /// </summary>
        [Input("PrimaryAvailabilityZone")]
        public Input<string>? PrimaryAvailabilityZone { get; set; }

        [Input("ReplicaAvailabilityZones")]
        private InputList<string>? _ReplicaAvailabilityZones;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-nodegroupconfiguration.html#cfn-elasticache-replicationgroup-nodegroupconfiguration-replicaavailabilityzones
        /// </summary>
        public InputList<string> ReplicaAvailabilityZones
        {
            get => _ReplicaAvailabilityZones ?? (_ReplicaAvailabilityZones = new InputList<string>());
            set => _ReplicaAvailabilityZones = value;
        }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-nodegroupconfiguration.html#cfn-elasticache-replicationgroup-nodegroupconfiguration-replicacount
        /// </summary>
        [Input("ReplicaCount")]
        public Input<int>? ReplicaCount { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-nodegroupconfiguration.html#cfn-elasticache-replicationgroup-nodegroupconfiguration-slots
        /// </summary>
        [Input("Slots")]
        public Input<string>? Slots { get; set; }

        public ReplicationGroupNodeGroupConfigurationArgs()
        {
        }
    }
}