// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Budgets.Outputs
{

    [OutputType]
    public sealed class BudgetTimePeriod
    {
        public readonly string? End;
        public readonly string? Start;

        [OutputConstructor]
        private BudgetTimePeriod(
            string? end,

            string? start)
        {
            End = end;
            Start = start;
        }
    }
}
