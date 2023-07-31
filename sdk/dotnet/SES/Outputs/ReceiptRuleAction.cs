// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SES.Outputs
{

    [OutputType]
    public sealed class ReceiptRuleAction
    {
        public readonly Outputs.ReceiptRuleAddHeaderAction? AddHeaderAction;
        public readonly Outputs.ReceiptRuleBounceAction? BounceAction;
        public readonly Outputs.ReceiptRuleLambdaAction? LambdaAction;
        public readonly Outputs.ReceiptRuleS3Action? S3Action;
        public readonly Outputs.ReceiptRuleSNSAction? SnsAction;
        public readonly Outputs.ReceiptRuleStopAction? StopAction;
        public readonly Outputs.ReceiptRuleWorkmailAction? WorkmailAction;

        [OutputConstructor]
        private ReceiptRuleAction(
            Outputs.ReceiptRuleAddHeaderAction? addHeaderAction,

            Outputs.ReceiptRuleBounceAction? bounceAction,

            Outputs.ReceiptRuleLambdaAction? lambdaAction,

            Outputs.ReceiptRuleS3Action? s3Action,

            Outputs.ReceiptRuleSNSAction? snsAction,

            Outputs.ReceiptRuleStopAction? stopAction,

            Outputs.ReceiptRuleWorkmailAction? workmailAction)
        {
            AddHeaderAction = addHeaderAction;
            BounceAction = bounceAction;
            LambdaAction = lambdaAction;
            S3Action = s3Action;
            SnsAction = snsAction;
            StopAction = stopAction;
            WorkmailAction = workmailAction;
        }
    }
}
