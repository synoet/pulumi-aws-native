// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.SecurityHub.Outputs
{

    [OutputType]
    public sealed class HubProperties
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-hub.html#cfn-securityhub-hub-tags
        /// </summary>
        public readonly Union<System.Text.Json.JsonElement, string>? Tags;

        [OutputConstructor]
        private HubProperties(Union<System.Text.Json.JsonElement, string>? Tags)
        {
            this.Tags = Tags;
        }
    }
}