// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.AuditManager.Outputs
{

    [OutputType]
    public sealed class AssessmentAttributes
    {
        public readonly string Arn;
        public readonly string AssessmentId;
        public readonly double CreationTime;
        public readonly Outputs.AssessmentDelegations Delegations;
        public readonly string FrameworkId;

        [OutputConstructor]
        private AssessmentAttributes(
            string arn,

            string assessmentId,

            double creationTime,

            Outputs.AssessmentDelegations delegations,

            string frameworkId)
        {
            Arn = arn;
            AssessmentId = assessmentId;
            CreationTime = creationTime;
            Delegations = delegations;
            FrameworkId = frameworkId;
        }
    }
}