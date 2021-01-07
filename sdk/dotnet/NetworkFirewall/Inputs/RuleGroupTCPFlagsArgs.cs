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
    /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-tcpflags.html
    /// </summary>
    public sealed class RuleGroupTCPFlagsArgs : Pulumi.ResourceArgs
    {
        [Input("TCPFlags")]
        private InputList<Inputs.RuleGroupTCPFlagFieldArgs>? _TCPFlags;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-tcpflags.html#cfn-networkfirewall-rulegroup-tcpflags-tcpflags
        /// </summary>
        public InputList<Inputs.RuleGroupTCPFlagFieldArgs> TCPFlags
        {
            get => _TCPFlags ?? (_TCPFlags = new InputList<Inputs.RuleGroupTCPFlagFieldArgs>());
            set => _TCPFlags = value;
        }

        public RuleGroupTCPFlagsArgs()
        {
        }
    }
}