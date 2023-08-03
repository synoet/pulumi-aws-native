// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Pipes.Outputs
{

    [OutputType]
    public sealed class PipeMskAccessCredentials0Properties
    {
        /// <summary>
        /// Optional SecretManager ARN which stores the database credentials
        /// </summary>
        public readonly string SaslScram512Auth;

        [OutputConstructor]
        private PipeMskAccessCredentials0Properties(string saslScram512Auth)
        {
            SaslScram512Auth = saslScram512Auth;
        }
    }
}
