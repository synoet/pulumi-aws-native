// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Budgets
{
    /// <summary>
    /// An example resource schema demonstrating some basic constructs and validation rules.
    /// </summary>
    [AwsNativeResourceType("aws-native:budgets:BudgetsAction")]
    public partial class BudgetsAction : global::Pulumi.CustomResource
    {
        [Output("actionId")]
        public Output<string> ActionId { get; private set; } = null!;

        [Output("actionThreshold")]
        public Output<Outputs.BudgetsActionActionThreshold> ActionThreshold { get; private set; } = null!;

        [Output("actionType")]
        public Output<Pulumi.AwsNative.Budgets.BudgetsActionActionType> ActionType { get; private set; } = null!;

        [Output("approvalModel")]
        public Output<Pulumi.AwsNative.Budgets.BudgetsActionApprovalModel?> ApprovalModel { get; private set; } = null!;

        [Output("budgetName")]
        public Output<string> BudgetName { get; private set; } = null!;

        [Output("definition")]
        public Output<Outputs.BudgetsActionDefinition> Definition { get; private set; } = null!;

        [Output("executionRoleArn")]
        public Output<string> ExecutionRoleArn { get; private set; } = null!;

        [Output("notificationType")]
        public Output<Pulumi.AwsNative.Budgets.BudgetsActionNotificationType> NotificationType { get; private set; } = null!;

        [Output("subscribers")]
        public Output<ImmutableArray<Outputs.BudgetsActionSubscriber>> Subscribers { get; private set; } = null!;


        /// <summary>
        /// Create a BudgetsAction resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public BudgetsAction(string name, BudgetsActionArgs args, CustomResourceOptions? options = null)
            : base("aws-native:budgets:BudgetsAction", name, args ?? new BudgetsActionArgs(), MakeResourceOptions(options, ""))
        {
        }

        private BudgetsAction(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:budgets:BudgetsAction", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "actionType",
                    "budgetName",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing BudgetsAction resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static BudgetsAction Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new BudgetsAction(name, id, options);
        }
    }

    public sealed class BudgetsActionArgs : global::Pulumi.ResourceArgs
    {
        [Input("actionThreshold", required: true)]
        public Input<Inputs.BudgetsActionActionThresholdArgs> ActionThreshold { get; set; } = null!;

        [Input("actionType", required: true)]
        public Input<Pulumi.AwsNative.Budgets.BudgetsActionActionType> ActionType { get; set; } = null!;

        [Input("approvalModel")]
        public Input<Pulumi.AwsNative.Budgets.BudgetsActionApprovalModel>? ApprovalModel { get; set; }

        [Input("budgetName", required: true)]
        public Input<string> BudgetName { get; set; } = null!;

        [Input("definition", required: true)]
        public Input<Inputs.BudgetsActionDefinitionArgs> Definition { get; set; } = null!;

        [Input("executionRoleArn", required: true)]
        public Input<string> ExecutionRoleArn { get; set; } = null!;

        [Input("notificationType", required: true)]
        public Input<Pulumi.AwsNative.Budgets.BudgetsActionNotificationType> NotificationType { get; set; } = null!;

        [Input("subscribers", required: true)]
        private InputList<Inputs.BudgetsActionSubscriberArgs>? _subscribers;
        public InputList<Inputs.BudgetsActionSubscriberArgs> Subscribers
        {
            get => _subscribers ?? (_subscribers = new InputList<Inputs.BudgetsActionSubscriberArgs>());
            set => _subscribers = value;
        }

        public BudgetsActionArgs()
        {
        }
        public static new BudgetsActionArgs Empty => new BudgetsActionArgs();
    }
}
