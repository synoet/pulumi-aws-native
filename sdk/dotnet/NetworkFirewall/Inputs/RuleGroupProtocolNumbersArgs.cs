// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.NetworkFirewall.Inputs
{

    /// <summary>
    /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-protocolnumbers.html
    /// </summary>
    public sealed class RuleGroupProtocolNumbersArgs : Pulumi.ResourceArgs
    {
        [Input("ProtocolNumbers")]
        private InputList<int>? _ProtocolNumbers;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-protocolnumbers.html#cfn-networkfirewall-rulegroup-protocolnumbers-protocolnumbers
        /// </summary>
        public InputList<int> ProtocolNumbers
        {
            get => _ProtocolNumbers ?? (_ProtocolNumbers = new InputList<int>());
            set => _ProtocolNumbers = value;
        }

        public RuleGroupProtocolNumbersArgs()
        {
        }
    }
}