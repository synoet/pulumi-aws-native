// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.IoTSiteWise.Inputs
{

    /// <summary>
    /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-accesspolicy.html
    /// </summary>
    public sealed class AccessPolicyPropertiesArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-accesspolicy.html#cfn-iotsitewise-accesspolicy-accesspolicyidentity
        /// </summary>
        [Input("AccessPolicyIdentity", required: true)]
        public Input<Inputs.AccessPolicyAccessPolicyIdentityArgs> AccessPolicyIdentity { get; set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-accesspolicy.html#cfn-iotsitewise-accesspolicy-accesspolicypermission
        /// </summary>
        [Input("AccessPolicyPermission", required: true)]
        public Input<string> AccessPolicyPermission { get; set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-accesspolicy.html#cfn-iotsitewise-accesspolicy-accesspolicyresource
        /// </summary>
        [Input("AccessPolicyResource", required: true)]
        public Input<Inputs.AccessPolicyAccessPolicyResourceArgs> AccessPolicyResource { get; set; } = null!;

        public AccessPolicyPropertiesArgs()
        {
        }
    }
}