// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.WAF.Inputs
{

    /// <summary>
    /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-ipset.html
    /// </summary>
    public sealed class IPSetPropertiesArgs : Pulumi.ResourceArgs
    {
        [Input("IPSetDescriptors")]
        private InputList<Inputs.IPSetIPSetDescriptorArgs>? _IPSetDescriptors;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-ipset.html#cfn-waf-ipset-ipsetdescriptors
        /// </summary>
        public InputList<Inputs.IPSetIPSetDescriptorArgs> IPSetDescriptors
        {
            get => _IPSetDescriptors ?? (_IPSetDescriptors = new InputList<Inputs.IPSetIPSetDescriptorArgs>());
            set => _IPSetDescriptors = value;
        }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-ipset.html#cfn-waf-ipset-name
        /// </summary>
        [Input("Name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public IPSetPropertiesArgs()
        {
        }
    }
}