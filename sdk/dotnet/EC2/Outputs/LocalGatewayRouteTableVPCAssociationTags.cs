// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.EC2.Outputs
{

    [OutputType]
    public sealed class LocalGatewayRouteTableVPCAssociationTags
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-localgatewayroutetablevpcassociation-tags.html#cfn-ec2-localgatewayroutetablevpcassociation-tags-tags
        /// </summary>
        public readonly ImmutableArray<Pulumi.Cloudformation.Outputs.Tag> Tags;

        [OutputConstructor]
        private LocalGatewayRouteTableVPCAssociationTags(ImmutableArray<Pulumi.Cloudformation.Outputs.Tag> Tags)
        {
            this.Tags = Tags;
        }
    }
}