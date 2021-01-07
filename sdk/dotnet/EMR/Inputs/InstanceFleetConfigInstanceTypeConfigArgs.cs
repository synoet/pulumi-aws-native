// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.EMR.Inputs
{

    /// <summary>
    /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-instancetypeconfig.html
    /// </summary>
    public sealed class InstanceFleetConfigInstanceTypeConfigArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-instancetypeconfig.html#cfn-elasticmapreduce-instancefleetconfig-instancetypeconfig-bidprice
        /// </summary>
        [Input("BidPrice")]
        public Input<string>? BidPrice { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-instancetypeconfig.html#cfn-elasticmapreduce-instancefleetconfig-instancetypeconfig-bidpriceaspercentageofondemandprice
        /// </summary>
        [Input("BidPriceAsPercentageOfOnDemandPrice")]
        public Input<double>? BidPriceAsPercentageOfOnDemandPrice { get; set; }

        [Input("Configurations")]
        private InputList<Inputs.InstanceFleetConfigConfigurationArgs>? _Configurations;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-instancetypeconfig.html#cfn-elasticmapreduce-instancefleetconfig-instancetypeconfig-configurations
        /// </summary>
        public InputList<Inputs.InstanceFleetConfigConfigurationArgs> Configurations
        {
            get => _Configurations ?? (_Configurations = new InputList<Inputs.InstanceFleetConfigConfigurationArgs>());
            set => _Configurations = value;
        }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-instancetypeconfig.html#cfn-elasticmapreduce-instancefleetconfig-instancetypeconfig-ebsconfiguration
        /// </summary>
        [Input("EbsConfiguration")]
        public Input<Inputs.InstanceFleetConfigEbsConfigurationArgs>? EbsConfiguration { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-instancetypeconfig.html#cfn-elasticmapreduce-instancefleetconfig-instancetypeconfig-instancetype
        /// </summary>
        [Input("InstanceType", required: true)]
        public Input<string> InstanceType { get; set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-instancetypeconfig.html#cfn-elasticmapreduce-instancefleetconfig-instancetypeconfig-weightedcapacity
        /// </summary>
        [Input("WeightedCapacity")]
        public Input<int>? WeightedCapacity { get; set; }

        public InstanceFleetConfigInstanceTypeConfigArgs()
        {
        }
    }
}