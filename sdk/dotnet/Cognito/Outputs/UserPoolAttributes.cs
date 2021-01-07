// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.Cognito.Outputs
{

    [OutputType]
    public sealed class UserPoolAttributes
    {
        public readonly string Arn;
        public readonly string ProviderName;
        public readonly string ProviderURL;

        [OutputConstructor]
        private UserPoolAttributes(
            string Arn,

            string ProviderName,

            string ProviderURL)
        {
            this.Arn = Arn;
            this.ProviderName = ProviderName;
            this.ProviderURL = ProviderURL;
        }
    }
}