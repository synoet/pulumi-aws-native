// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ec2
{
    public static class GetKeyPair
    {
        /// <summary>
        /// The AWS::EC2::KeyPair creates an SSH key pair
        /// </summary>
        public static Task<GetKeyPairResult> InvokeAsync(GetKeyPairArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetKeyPairResult>("aws-native:ec2:getKeyPair", args ?? new GetKeyPairArgs(), options.WithDefaults());

        /// <summary>
        /// The AWS::EC2::KeyPair creates an SSH key pair
        /// </summary>
        public static Output<GetKeyPairResult> Invoke(GetKeyPairInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetKeyPairResult>("aws-native:ec2:getKeyPair", args ?? new GetKeyPairInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetKeyPairArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the SSH key pair
        /// </summary>
        [Input("keyName", required: true)]
        public string KeyName { get; set; } = null!;

        public GetKeyPairArgs()
        {
        }
        public static new GetKeyPairArgs Empty => new GetKeyPairArgs();
    }

    public sealed class GetKeyPairInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the SSH key pair
        /// </summary>
        [Input("keyName", required: true)]
        public Input<string> KeyName { get; set; } = null!;

        public GetKeyPairInvokeArgs()
        {
        }
        public static new GetKeyPairInvokeArgs Empty => new GetKeyPairInvokeArgs();
    }


    [OutputType]
    public sealed class GetKeyPairResult
    {
        /// <summary>
        /// A short sequence of bytes used for public key verification
        /// </summary>
        public readonly string? KeyFingerprint;
        /// <summary>
        /// An AWS generated ID for the key pair
        /// </summary>
        public readonly string? KeyPairId;

        [OutputConstructor]
        private GetKeyPairResult(
            string? keyFingerprint,

            string? keyPairId)
        {
            KeyFingerprint = keyFingerprint;
            KeyPairId = keyPairId;
        }
    }
}
