// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.IoT.Outputs
{

    [OutputType]
    public sealed class ThingProperties
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thing.html#cfn-iot-thing-attributepayload
        /// </summary>
        public readonly Outputs.ThingAttributePayload? AttributePayload;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thing.html#cfn-iot-thing-thingname
        /// </summary>
        public readonly string? ThingName;

        [OutputConstructor]
        private ThingProperties(
            Outputs.ThingAttributePayload? AttributePayload,

            string? ThingName)
        {
            this.AttributePayload = AttributePayload;
            this.ThingName = ThingName;
        }
    }
}