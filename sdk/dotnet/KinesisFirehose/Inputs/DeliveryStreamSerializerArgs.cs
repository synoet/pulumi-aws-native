// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.KinesisFirehose.Inputs
{

    /// <summary>
    /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-serializer.html
    /// </summary>
    public sealed class DeliveryStreamSerializerArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-serializer.html#cfn-kinesisfirehose-deliverystream-serializer-orcserde
        /// </summary>
        [Input("OrcSerDe")]
        public Input<Inputs.DeliveryStreamOrcSerDeArgs>? OrcSerDe { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-serializer.html#cfn-kinesisfirehose-deliverystream-serializer-parquetserde
        /// </summary>
        [Input("ParquetSerDe")]
        public Input<Inputs.DeliveryStreamParquetSerDeArgs>? ParquetSerDe { get; set; }

        public DeliveryStreamSerializerArgs()
        {
        }
    }
}