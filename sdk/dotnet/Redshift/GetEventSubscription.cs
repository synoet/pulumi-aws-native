// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Redshift
{
    public static class GetEventSubscription
    {
        /// <summary>
        /// The `AWS::Redshift::EventSubscription` resource creates an Amazon Redshift Event Subscription.
        /// </summary>
        public static Task<GetEventSubscriptionResult> InvokeAsync(GetEventSubscriptionArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetEventSubscriptionResult>("aws-native:redshift:getEventSubscription", args ?? new GetEventSubscriptionArgs(), options.WithDefaults());

        /// <summary>
        /// The `AWS::Redshift::EventSubscription` resource creates an Amazon Redshift Event Subscription.
        /// </summary>
        public static Output<GetEventSubscriptionResult> Invoke(GetEventSubscriptionInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetEventSubscriptionResult>("aws-native:redshift:getEventSubscription", args ?? new GetEventSubscriptionInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetEventSubscriptionArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the Amazon Redshift event notification subscription
        /// </summary>
        [Input("subscriptionName", required: true)]
        public string SubscriptionName { get; set; } = null!;

        public GetEventSubscriptionArgs()
        {
        }
        public static new GetEventSubscriptionArgs Empty => new GetEventSubscriptionArgs();
    }

    public sealed class GetEventSubscriptionInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the Amazon Redshift event notification subscription
        /// </summary>
        [Input("subscriptionName", required: true)]
        public Input<string> SubscriptionName { get; set; } = null!;

        public GetEventSubscriptionInvokeArgs()
        {
        }
        public static new GetEventSubscriptionInvokeArgs Empty => new GetEventSubscriptionInvokeArgs();
    }


    [OutputType]
    public sealed class GetEventSubscriptionResult
    {
        /// <summary>
        /// The name of the Amazon Redshift event notification subscription.
        /// </summary>
        public readonly string? CustSubscriptionId;
        /// <summary>
        /// The AWS account associated with the Amazon Redshift event notification subscription.
        /// </summary>
        public readonly string? CustomerAwsId;
        /// <summary>
        /// A boolean value; set to true to activate the subscription, and set to false to create the subscription but not activate it.
        /// </summary>
        public readonly bool? Enabled;
        /// <summary>
        /// Specifies the Amazon Redshift event categories to be published by the event notification subscription.
        /// </summary>
        public readonly ImmutableArray<Pulumi.AwsNative.Redshift.EventSubscriptionEventCategoriesItem> EventCategories;
        /// <summary>
        /// The list of Amazon Redshift event categories specified in the event notification subscription.
        /// </summary>
        public readonly ImmutableArray<string> EventCategoriesList;
        /// <summary>
        /// Specifies the Amazon Redshift event severity to be published by the event notification subscription.
        /// </summary>
        public readonly Pulumi.AwsNative.Redshift.EventSubscriptionSeverity? Severity;
        /// <summary>
        /// The Amazon Resource Name (ARN) of the Amazon SNS topic used to transmit the event notifications.
        /// </summary>
        public readonly string? SnsTopicArn;
        /// <summary>
        /// A list of one or more identifiers of Amazon Redshift source objects.
        /// </summary>
        public readonly ImmutableArray<string> SourceIds;
        /// <summary>
        /// A list of the sources that publish events to the Amazon Redshift event notification subscription.
        /// </summary>
        public readonly ImmutableArray<string> SourceIdsList;
        /// <summary>
        /// The type of source that will be generating the events.
        /// </summary>
        public readonly Pulumi.AwsNative.Redshift.EventSubscriptionSourceType? SourceType;
        /// <summary>
        /// The status of the Amazon Redshift event notification subscription.
        /// </summary>
        public readonly Pulumi.AwsNative.Redshift.EventSubscriptionStatus? Status;
        /// <summary>
        /// The date and time the Amazon Redshift event notification subscription was created.
        /// </summary>
        public readonly string? SubscriptionCreationTime;

        [OutputConstructor]
        private GetEventSubscriptionResult(
            string? custSubscriptionId,

            string? customerAwsId,

            bool? enabled,

            ImmutableArray<Pulumi.AwsNative.Redshift.EventSubscriptionEventCategoriesItem> eventCategories,

            ImmutableArray<string> eventCategoriesList,

            Pulumi.AwsNative.Redshift.EventSubscriptionSeverity? severity,

            string? snsTopicArn,

            ImmutableArray<string> sourceIds,

            ImmutableArray<string> sourceIdsList,

            Pulumi.AwsNative.Redshift.EventSubscriptionSourceType? sourceType,

            Pulumi.AwsNative.Redshift.EventSubscriptionStatus? status,

            string? subscriptionCreationTime)
        {
            CustSubscriptionId = custSubscriptionId;
            CustomerAwsId = customerAwsId;
            Enabled = enabled;
            EventCategories = eventCategories;
            EventCategoriesList = eventCategoriesList;
            Severity = severity;
            SnsTopicArn = snsTopicArn;
            SourceIds = sourceIds;
            SourceIdsList = sourceIdsList;
            SourceType = sourceType;
            Status = status;
            SubscriptionCreationTime = subscriptionCreationTime;
        }
    }
}
